import axios from 'axios';

export const getDocuments = async (prompt) => {
    try {
        const response = await axios.post('/api/RetrieveDocuments', { query: prompt });
        return response.data.documents;
    } catch (error) {
        console.error("Error retrieving documents:", error);
        throw error;
    }
};
