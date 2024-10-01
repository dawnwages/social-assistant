import { getDocuments } from './RAGService';

export default {
  async getCompletion(messages, groundingSource, temperature, burkeMode) {
    // Step 1: Create an array that contains only the role and content properties of each message
    const completionMessages = messages.map((message) => {
      return {
        role: message.role,
        content: message.content
      };
    });

    // retrieve relevant documents (RAG) based on the messages
    let retrievedDocuments = [];
    try {
      const userMessage = messages.find(message => message.role === 'user')?.content;
      if (userMessage) {
        retrievedDocuments = await getDocuments(userMessage);
      }
    } catch (error) {
      console.error('Error fetching documents with RAG:', error);
      return {
        status: 500,
        content: 'Error fetching grounding documents. Please try again later.'
      };
    }

    // send both the original messages and retrieved documents to the completion API
    const result = await fetch('/api/completion', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        groundingSource: groundingSource,
        messages: completionMessages,
        temperature: temperature,
        burkeMode: burkeMode,
        documents: retrievedDocuments // Include retrieved documents in the completion request
      })
    });

    // handle response from the completion API
    if (result.status === 500) {
      return {
        status: result.status,
        content: 'The server returned an internal error. This happens with the Azure OpenAI services sometimes. Try your request again.'
      };
    }

    const data = await result.json();

    if (result.status !== 200) {
      return {
        status: result.status,
        content: data.body
      };
    }

    return {
      status: 200,
      usedTokens: data.usedTokens,
      content: data.content,
      contentPlain: data.contentPlain
    };
  }
};
