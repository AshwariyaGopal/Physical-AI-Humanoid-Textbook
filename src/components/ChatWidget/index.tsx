import React, { useState, useRef, useEffect } from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './styles.module.css';

interface Source {
  url: string;
  title?: string;
  chunk_index: number;
}

interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: number;
  sources?: Source[];
}

const ChatWidget: React.FC = () => {
  const { siteConfig } = useDocusaurusContext();
  const backendUrl = siteConfig.customFields?.backendUrl as string || 'http://localhost:8000';

  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const messageListRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom when messages change
  useEffect(() => {
    if (messageListRef.current) {
      messageListRef.current.scrollTop = messageListRef.current.scrollHeight;
    }
  }, [messages]);

  const toggleChat = () => setIsOpen(!isOpen);

  const handleSend = async () => {
    if (!inputValue.trim()) return;

    const userMessage: ChatMessage = {
      id: Date.now().toString(),
      role: 'user',
      content: inputValue,
      timestamp: Date.now(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setInputValue('');
    setError(null);
    setIsLoading(true);

    try {
      const response = await fetch(`https://ashwariyagopal-rag-chatbot.hf.space/ask`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userMessage.content }),
      });

      if (!response.ok) {
        throw new Error(`Server responded with ${response.status}`);
      }

      const data = await response.json();

      const assistantMessage: ChatMessage = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: data.answer,
        timestamp: Date.now(),
        sources: data.sources,
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch (err: any) {
      setError(err.message || 'Failed to connect to assistant');
    } finally {
      setIsLoading(false);
    }
  };

  if (!isOpen) {
    return (
      <button className={styles.chatToggleButton} onClick={toggleChat} style={{
        position: 'fixed',
        bottom: '20px',
        right: '20px',
        padding: '12px 20px',
        borderRadius: '50px',
        backgroundColor: 'var(--ifm-color-primary)',
        color: 'white',
        border: 'none',
        cursor: 'pointer',
        boxShadow: '0 4px 12px rgba(0,0,0,0.15)',
        zIndex: 1000
      }}>
        Ask Assistant
      </button>
    );
  }

  return (
    <div className={styles.chatWidget}>
      <div className={styles.chatHeader}>
        <span>AI Textbook Assistant</span>
        <button onClick={toggleChat} style={{ background: 'none', border: 'none', color: 'white', cursor: 'pointer', fontSize: '1.2rem' }}>×</button>
      </div>
      
      <div className={styles.messageList} ref={messageListRef}>
        {messages.length === 0 && (
          <div style={{ textAlign: 'center', color: 'var(--ifm-color-emphasis-600)', marginTop: '20px' }}>
            Ask me anything about the textbook!
          </div>
        )}
        {messages.map((msg) => (
          <div key={msg.id} className={`${styles.message} ${msg.role === 'user' ? styles.userMessage : styles.assistantMessage}`}>
            <div>{msg.content}</div>
            {msg.sources && msg.sources.length > 0 && (
              <div className={styles.sources}>
                <strong>Sources:</strong>
                <ul>
                  {msg.sources.map((src, idx) => (
                    <li key={idx}>
                      <a href={src.url} target="_blank" rel="noopener noreferrer">
                        {src.title || `Source ${idx + 1}`}
                      </a>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ))}
        {isLoading && <div className={styles.loading}>Assistant is thinking...</div>}
        {error && <div className={styles.error}>{error}</div>}
      </div>

      <div className={styles.inputArea}>
        <input
          type="text"
          className={styles.inputField}
          placeholder="Type your question..."
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && !isLoading && handleSend()}
        />
        <button 
          className={styles.sendButton} 
          onClick={handleSend}
          disabled={isLoading || !inputValue.trim()}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatWidget;