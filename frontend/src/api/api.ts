import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

export const uploadFile = async (file: File) => {
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await axios.post(`${API_BASE_URL}/upload`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    return response.data;
  } catch (error) {
    console.error('Error uploading file:', error);
    throw error;
  }
};

// export const fetchDocuments = async () => {
//   try {
//     const response = await axios.get(`${API_BASE_URL}/documents`);
//     return response.data;
//   } catch (error) {
//     console.error('Error fetching documents:', error);
//     throw error;
//   }
// };

// export const getSummary = async (docId: string) => {
//   try {
//     const response = await axios.get(`${API_BASE_URL}/summary/${docId}`);
//     return response.data;
//   } catch (error) {
//     console.error('Error fetching summary:', error);
//     throw error;
//   }
// };

export const sendMessage = async (message: string) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/chat`, { message });
    return response.data;
  } catch (error) {
    console.error('Error sending message:', error);
    throw error;
  }
};
