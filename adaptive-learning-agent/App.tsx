import React, { useState, useCallback } from 'react';
import { LearningPreferences, LearningPathway } from './types';
import { generateLearningPathway } from './services/geminiService';
import InputForm from './components/InputForm';
import LoadingModal from './components/LoadingModal';
import PathwayDisplay from './components/PathwayDisplay';
import { Footer } from './components/Footer';

type AppState = 'form' | 'loading' | 'results';

const App: React.FC = () => {
  const [appState, setAppState] = useState<AppState>('form');
  const [pathway, setPathway] = useState<LearningPathway | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleGeneratePathway = useCallback(async (preferences: LearningPreferences) => {
    setAppState('loading');
    setError(null);
    try {
      const generatedPathway = await generateLearningPathway(preferences);
      setPathway(generatedPathway);
      setAppState('results');
    } catch (err) {
      console.error(err);
      setError('Failed to generate learning pathway. Please check your connection and try again.');
      setAppState('form');
    }
  }, []);

  const handleTryAgain = () => {
    setAppState('form');
    setPathway(null);
    setError(null);
  };

  return (
    <div className="min-h-screen bg-slate-900 text-gray-200 font-['Inter',_sans-serif]">
      <div className="relative isolate min-h-screen flex flex-col">
        <div className="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80" aria-hidden="true">
          <div className="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#0d043c] to-[#0c3a6d] opacity-20 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]" style={{ clipPath: 'polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)' }}></div>
        </div>
        
        <main className="container mx-auto px-4 py-8 md:py-16 flex-grow flex flex-col items-center justify-center">
          {appState === 'form' && <InputForm onGenerate={handleGeneratePathway} error={error} />}
          {appState === 'loading' && <LoadingModal />}
          {appState === 'results' && pathway && <PathwayDisplay pathway={pathway} onTryAgain={handleTryAgain} />}
        </main>
        
        <div className="absolute inset-x-0 top-[calc(100%-13rem)] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[calc(100%-40rem)]" aria-hidden="true">
          <div className="relative left-[calc(50%+3rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 bg-gradient-to-tr from-[#0c3a6d] to-[#0d043c] opacity-20 sm:left-[calc(50%+36rem)] sm:w-[72.1875rem]" style={{ clipPath: 'polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)' }}></div>
        </div>

        <Footer />
      </div>
    </div>
  );
};

export default App;