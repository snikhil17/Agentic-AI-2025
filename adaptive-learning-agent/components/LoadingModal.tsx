import React, { useState, useEffect } from 'react';

const loadingMessages = [
  "Igniting neural networks...",
  "Curating personalized content...",
  "Connecting concepts to your hobbies...",
  "Designing your learning phases...",
  "Finding the best real-world examples...",
  "Finalizing your unique pathway...",
];

const LoadingModal: React.FC = () => {
  const [progress, setProgress] = useState(0);
  const [messageIndex, setMessageIndex] = useState(0);

  useEffect(() => {
    const progressInterval = setInterval(() => {
      setProgress(prev => (prev >= 95 ? 95 : prev + 2));
    }, 400);

    const messageInterval = setInterval(() => {
      setMessageIndex(prev => (prev + 1) % loadingMessages.length);
    }, 2500);

    return () => {
      clearInterval(progressInterval);
      clearInterval(messageInterval);
    };
  }, []);

  return (
    <div className="fixed inset-0 bg-slate-900 bg-opacity-70 backdrop-blur-sm flex items-center justify-center z-50 transition-opacity duration-300">
      <div className="bg-slate-800 rounded-2xl shadow-2xl p-8 w-full max-w-md text-center transform transition-all duration-300 scale-100 border border-slate-700">
        <div className="w-16 h-16 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto mb-6"></div>
        <h2 className="text-2xl font-bold text-white mb-4">Crafting Your Pathway</h2>
        <p className="text-slate-300 mb-6 min-h-[2.5rem]">{loadingMessages[messageIndex]}</p>
        <div className="w-full bg-slate-700 rounded-full h-4 overflow-hidden">
          <div
            className="bg-gradient-to-r from-blue-500 to-purple-500 h-4 rounded-full transition-all duration-500 ease-out"
            style={{ width: `${progress}%` }}
          ></div>
        </div>
      </div>
    </div>
  );
};

export default LoadingModal;