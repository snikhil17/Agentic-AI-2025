import React, { useState } from 'react';
import type { LearningPreferences } from '../types';
import { BookIcon, HobbyIcon, DomainIcon, StyleIcon, SparklesIcon, HistoryIcon, LinkIcon } from './Icons';

interface InputFormProps {
  onGenerate: (preferences: LearningPreferences) => void;
  error: string | null;
}

const InputField: React.FC<{ id: string, label: string, value: string, onChange: (e: React.ChangeEvent<HTMLInputElement>) => void, placeholder: string, icon: React.ReactNode, type?: string }> = ({ id, label, value, onChange, placeholder, icon, type = "text" }) => (
  <div>
    <label htmlFor={id} className="flex items-center text-md font-medium text-slate-300 mb-2">
      {icon}
      {label}
    </label>
    <input
      type={type}
      id={id}
      name={id}
      value={value}
      onChange={onChange}
      placeholder={placeholder}
      className="w-full px-4 py-3 bg-slate-700/50 border border-slate-600 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all placeholder-slate-400 text-white"
      required
    />
  </div>
);

const FeatureCard: React.FC<{icon: React.ReactNode, title: string}> = ({icon, title}) => (
    <div className="flex flex-col items-center text-center p-4">
        <div className="flex items-center justify-center h-12 w-12 rounded-full bg-slate-700/50 mb-3">
            {icon}
        </div>
        <p className="font-semibold text-slate-200">{title}</p>
    </div>
);


const InputForm: React.FC<InputFormProps> = ({ onGenerate, error }) => {
  const [preferences, setPreferences] = useState<LearningPreferences>({
    learningStyle: 'Intuitive real-world examples',
    topic: 'generative AI',
    hobbies: 'watching friends on Netflix',
    domain: 'finance',
    googleApiKey: '',
    tavilyApiKey: '',
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setPreferences(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onGenerate(preferences);
  };

  return (
    <div className="w-full max-w-3xl">
      <div className="bg-slate-800/30 backdrop-blur-2xl p-8 md:p-12 rounded-2xl shadow-2xl border border-slate-700">
        <div className="text-center mb-8">
          <h1 className="text-4xl md:text-5xl font-bold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-400">Agentic AI Learning Assistant</h1>
          <p className="mt-4 text-lg text-slate-300 leading-relaxed max-w-2xl mx-auto">
            Imagine learning any topic effortlessly—tailored exactly to you. Just enter your preferences, and let our AI-powered assistant do the rest.
          </p>
        </div>

        <div className="mb-8 p-6 bg-slate-900/40 rounded-lg">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
              <FeatureCard icon={<HistoryIcon />} title="Engaging History & Milestones" />
              <FeatureCard icon={<HobbyIcon />} title="Customized Examples" />
              <FeatureCard icon={<DomainIcon />} title="Real-world Projects" />
              <FeatureCard icon={<LinkIcon />} title="Handpicked Links" />
          </div>
        </div>

        <p className="text-center text-slate-300 mb-6 font-medium">Start your personalized learning journey now!</p>

        {error && (
          <div className="bg-red-900/50 border border-red-500 text-red-300 p-4 mb-6 rounded-lg" role="alert">
            <p className="font-bold">Error</p>
            <p>{error}</p>
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-6">
          <InputField id="learningStyle" label="Preferred Learning Style" value={preferences.learningStyle} onChange={handleChange} placeholder="e.g., Visual learner, project-based" icon={<StyleIcon />} />
          <InputField id="topic" label="Learning Topic / Subject" value={preferences.topic} onChange={handleChange} placeholder="e.g., Quantum Computing, History of Rome" icon={<BookIcon />} />
          <InputField id="hobbies" label="Hobbies" value={preferences.hobbies} onChange={handleChange} placeholder="e.g., Playing guitar, hiking, video games" icon={<HobbyIcon />} />
          <InputField id="domain" label="Domain / Field of Interest" value={preferences.domain} onChange={handleChange} placeholder="e.g., Healthcare, software development" icon={<DomainIcon />} />
          
          <div className="bg-slate-900/40 p-6 rounded-lg border border-slate-600">
            <h3 className="text-lg font-semibold text-slate-200 mb-4 flex items-center gap-2">
              🔑 API Keys Required
            </h3>
            <p className="text-slate-400 text-sm mb-4">
              This app requires API keys to generate personalized content. Your keys are sent directly to the backend and not stored.
            </p>
            <div className="space-y-4">
              <InputField 
                id="googleApiKey" 
                label="Google API Key (Gemini)" 
                value={preferences.googleApiKey} 
                onChange={handleChange} 
                placeholder="Your Google AI Studio API key" 
                icon={<SparklesIcon />} 
                type="password"
              />
              <InputField 
                id="tavilyApiKey" 
                label="Tavily API Key" 
                value={preferences.tavilyApiKey} 
                onChange={handleChange} 
                placeholder="Your Tavily search API key" 
                icon={<SparklesIcon />} 
                type="password"
              />
            </div>
            <div className="mt-3 text-xs text-slate-400">
              <p>• Get Google API key: <a href="https://ai.google.dev/" target="_blank" rel="noopener noreferrer" className="text-blue-400 hover:underline">Google AI Studio</a></p>
              <p>• Get Tavily API key: <a href="https://app.tavily.com/" target="_blank" rel="noopener noreferrer" className="text-blue-400 hover:underline">Tavily Dashboard</a></p>
            </div>
          </div>
          
          <button type="submit" className="w-full flex justify-center items-center gap-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white font-bold text-lg py-4 px-6 rounded-lg shadow-lg hover:from-blue-500 hover:to-purple-500 focus:outline-none focus:ring-4 focus:ring-blue-400/50 transition-all transform hover:scale-[1.02] hover:shadow-[0_0_20px_rgba(96,165,250,0.5)]">
            <SparklesIcon />
            Generate Learning Pathway
          </button>
        </form>
      </div>
    </div>
  );
};

export default InputForm;