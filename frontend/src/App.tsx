import React, { useState, useEffect, useRef } from 'react';
import { uploadFile, sendMessage } from './api/api';

import {
  FileUp,
  Send,
  FileText,
  Pin,
  MessageSquare,
  Volume2,
  FileDown,
  Plus,
  ChevronRight,
  Moon,
  Sun
} from 'lucide-react';

interface Document {
  id: string;
  name: string;
  selected: boolean;
}

interface ChatMessage {
  id: string;
  content: string;
  sender: "system" | "user";
  loading?: boolean;
}

function App() {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [inputMessage, setInputMessage] = useState(''); // no longer used for sending messages
  const [darkMode, setDarkMode] = useState(false);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const chatEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Auto-scroll to the bottom whenever messages change
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];

    if (file && file.type === 'application/pdf') {
      const response = await uploadFile(file);
      console.log("Upload successful:", response);

      const newDoc: Document = {
        id: Math.random().toString(36).substr(2, 9),
        name: file.name,
        selected: true,
      };
      setDocuments([...documents, newDoc]);
    }
  };

  // Existing function for sending a message (retained for reference)
  const handleSendMessage = async () => {
    if (inputMessage.trim()) {
      try {
        const response = await sendMessage(inputMessage);
        console.log('Message sent successfully:', response);
        // Optionally, update your UI or state based on the response
      } catch (error) {
        console.error('Error sending message:', error);
      }
      setInputMessage('');
    }
  };

  // Updated function for the Briefing Doc button with loading and summary display
  const handleBriefingDoc = async () => {
    // Add a loading message to the chat
    const loadingMessageId = Math.random().toString(36).substr(2, 9);
    setMessages(prev => [
      ...prev,
      { id: loadingMessageId, content: "Loading summary...", sender: "system", loading: true }
    ]);

    try {
      // Call the API to get the summary
      const response = await sendMessage("briefing doc");
      // Extract a string from the response: check for "response" then "summary"
      const summaryText =
        typeof response === "string"
          ? response
          : response.response || response || "No summary available.";

      // Update the loading message with the summary text
      setMessages(prev =>
        prev.map(msg =>
          msg.id === loadingMessageId ? { ...msg, content: summaryText, loading: false } : msg
        )
      );
      console.log('Briefing Doc API request sent successfully:', response);
    } catch (error) {
      console.error('Error sending Briefing Doc request:', error);
      setMessages(prev =>
        prev.map(msg =>
          msg.id === loadingMessageId ? { ...msg, content: "Error loading summary.", loading: false } : msg
        )
      );
    }
  };

  const toggleDocument = (id: string) => {
    setDocuments(docs =>
      docs.map(doc =>
        doc.id === id ? { ...doc, selected: !doc.selected } : doc
      )
    );
  };

  const toggleDarkMode = () => setDarkMode(!darkMode);

  return (
    <div className={`flex h-screen ${darkMode ? 'bg-gray-900' : 'bg-gray-50'} transition-colors duration-200`}>
      {/* Left Panel - Sources */}
      <div className={`w-1/3 min-w-[300px] max-w-md ${darkMode ? 'bg-gray-800' : 'bg-white'} shadow-xl border-r ${darkMode ? 'border-gray-700' : 'border-gray-200'}`}>
        <div className="flex flex-col h-full">
          <div className={`p-6 border-b ${darkMode ? 'border-gray-700' : 'border-gray-200'}`}>
            <div className="flex justify-between items-center mb-6">
              <h2 className={`text-xl font-semibold ${darkMode ? 'text-white' : 'text-gray-800'}`}>Sources</h2>
              <button
                onClick={toggleDarkMode}
                className={`p-2 rounded-full ${darkMode ? 'hover:bg-gray-700' : 'hover:bg-gray-100'} transition-colors`}
              >
                {darkMode ? <Sun className="w-5 h-5 text-gray-400" /> : <Moon className="w-5 h-5 text-gray-600" />}
              </button>
            </div>
            <label className={`flex items-center justify-center w-full p-4 border-2 border-dashed rounded-xl cursor-pointer transition-all hover:scale-[1.02] ${
              darkMode 
                ? 'border-blue-500/30 bg-blue-500/10 hover:bg-blue-500/20' 
                : 'border-blue-200 bg-blue-50 hover:bg-blue-100'
            }`}>
              <div className="flex items-center gap-3">
                <Plus className={`w-5 h-5 ${darkMode ? 'text-blue-400' : 'text-blue-600'}`} />
                <span className={`font-medium ${darkMode ? 'text-blue-400' : 'text-blue-600'}`}>Add Source</span>
              </div>
              <input
                type="file"
                accept=".pdf"
                onChange={handleFileUpload}
                className="hidden"
              />
            </label>
          </div>

          <div className="flex-1 overflow-y-auto p-4 space-y-2">
            {documents.map(doc => (
              <div
                key={doc.id}
                className={`flex items-center gap-3 p-4 rounded-lg group transition-colors ${
                  darkMode 
                    ? 'hover:bg-gray-700/50' 
                    : 'hover:bg-gray-50'
                } border ${
                  darkMode 
                    ? 'border-gray-700' 
                    : 'border-gray-100'
                }`}
              >
                <input
                  type="checkbox"
                  checked={doc.selected}
                  onChange={() => toggleDocument(doc.id)}
                  className="w-4 h-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                />
                <FileText className={`w-5 h-5 ${darkMode ? 'text-gray-400' : 'text-gray-500'}`} />
                <span className={`flex-1 truncate ${darkMode ? 'text-gray-300' : 'text-gray-700'}`}>{doc.name}</span>
                <ChevronRight className={`w-4 h-4 ${darkMode ? 'text-gray-500' : 'text-gray-400'} opacity-0 group-hover:opacity-100 transition-opacity`} />
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Right Panel - Main Content */}
      <div className="flex-1 flex flex-col overflow-hidden">
        <div className={`p-8 ${darkMode ? 'bg-gray-800' : 'bg-white'} shadow-lg`}>
          <div className="max-w-3xl mx-auto">
            <div className={`flex flex-col items-center p-8 rounded-2xl shadow-lg mb-8 ${
              darkMode ? 'bg-gray-700/50' : 'bg-white'
            }`}>
              <FileText className={`w-16 h-16 ${darkMode ? 'text-blue-400' : 'text-blue-600'} mb-4`} />
              <h1 className={`text-2xl font-bold text-center ${darkMode ? 'text-white' : 'text-gray-900'}`}>
                Mark Chandler: Implant Records and Medical History
              </h1>
            </div>

            <div className={`rounded-xl p-6 mb-8 ${
              darkMode ? 'bg-gray-700/50' : 'bg-gray-50'
            }`}>
              <p className={`leading-relaxed ${darkMode ? 'text-gray-300' : 'text-gray-700'}`}>
                This document contains detailed medical records and implant history for Mark Chandler,
                including procedures performed, dates, and relevant medical observations. The records
                span from 2020 to present day.
              </p>
            </div>

            <div className="flex flex-wrap gap-3 mb-8">
              {[
                { icon: Pin, label: 'Save to Note' },
                { icon: MessageSquare, label: 'Add Note' },
                { icon: Volume2, label: 'Audio Overview' },
                { icon: FileDown, label: 'Briefing Doc' }
              ].map(({ icon: Icon, label }) => (
                <button
                  key={label}
                  // For "Briefing Doc", attach the new handler that shows a loading bubble and then updates it with the summary.
                  onClick={label === 'Briefing Doc' ? handleBriefingDoc : undefined}
                  className={`flex items-center gap-2 px-5 py-3 rounded-lg transition-all hover:scale-[1.02] ${
                    darkMode
                      ? 'bg-gray-700 hover:bg-gray-600 text-gray-200'
                      : 'bg-gray-100 hover:bg-gray-200 text-gray-700'
                  } shadow-sm`}
                >
                  <Icon className="w-4 h-4" />
                  <span className="font-medium">{label}</span>
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Chat messages panel */}
        <div className={`flex-1 overflow-y-auto p-8 ${darkMode ? 'bg-gray-900' : 'bg-gray-50'}`}>
          <div className="max-w-3xl mx-auto flex flex-col space-y-4">
            {messages.map(msg => (
              <div
                key={msg.id}
                className={`p-4 rounded-lg max-w-md ${darkMode ? 'bg-gray-800 text-white' : 'bg-gray-100 text-gray-800'} ${msg.sender === 'system' ? 'self-start' : 'self-end'}`}
              >
                <p>{msg.content}</p>
                {msg.loading && <span className="text-xs text-gray-500">Loading...</span>}
              </div>
            ))}
            <div ref={chatEndRef} />
          </div>
        </div>

        {/*
        // Commented out the chat input area with text field and Send button
        <div className={`p-8 ${darkMode ? 'bg-gray-800 border-gray-700' : 'bg-white border-gray-200'} border-t`}>
          <div className="max-w-3xl mx-auto">
            <div className="flex gap-3">
              <input
                type="text"
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                placeholder="Start typing..."
                className={`flex-1 px-4 py-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-colors ${
                  darkMode
                    ? 'bg-gray-700 border-gray-600 text-white placeholder-gray-400'
                    : 'bg-white border-gray-300 text-gray-900 placeholder-gray-500'
                }`}
                onKeyPress={(e) => {
                  if (e.key === 'Enter') {
                    e.preventDefault();
                    handleSendMessage();
                  }
                }}
              />
              <button
                onClick={handleSendMessage}
                className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-all hover:scale-[1.02] shadow-sm flex items-center gap-2"
              >
                <Send className="w-4 h-4" />
                <span className="font-medium">Send</span>
              </button>
            </div>
          </div>
        </div>
        */}
      </div>
    </div>
  );
}

export default App;
