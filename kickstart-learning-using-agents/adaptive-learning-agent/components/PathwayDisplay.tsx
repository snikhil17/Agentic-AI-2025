import React from 'react';
import ReactMarkdown from 'react-markdown';
import type { LearningPathway } from '../types';
import { ArrowIcon, CheckIcon, HistoryIcon, LinkIcon, NextIcon, PhaseIcon, SparklesIcon } from './Icons';

interface PathwayDisplayProps {
  pathway: LearningPathway;
  onTryAgain: () => void;
}

const Card: React.FC<{ title: string; children: React.ReactNode; icon: React.ReactNode; }> = ({ title, children, icon }) => (
    <div className="bg-slate-800/30 backdrop-blur-lg rounded-xl shadow-lg border border-slate-700 overflow-hidden mb-8">
        <div className="p-6 bg-slate-900/30 border-b border-slate-700">
            <h2 className="text-2xl font-bold text-white flex items-center gap-3">
                {icon}
                {title}
            </h2>
        </div>
        <div className="p-6 space-y-4 text-slate-200 leading-relaxed">
            {children}
        </div>
    </div>
);


const PathwayDisplay: React.FC<PathwayDisplayProps> = ({ pathway, onTryAgain }) => {
  return (
    <div className="w-full max-w-4xl animate-fade-in">
        <div className="text-center mb-12">
            <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-400">{pathway.title}</h1>
            <p className="mt-4 text-xl text-slate-300 max-w-3xl mx-auto">{pathway.introduction}</p>
        </div>

        {pathway.phases.map((phase, index) => (
            <Card key={index} title={phase.title} icon={<PhaseIcon />}>
                <p className="italic text-slate-400 mb-6">{phase.description}</p>
                <ol className="space-y-6">
                    {phase.steps.map((step, stepIndex) => (
                        <li key={stepIndex} className="p-4 border border-slate-700 rounded-lg bg-slate-900/30">
                            <h4 className="font-bold text-lg text-white">{step.title}</h4>
                            <div className="mt-2 markdown-content">
                                <ReactMarkdown>{step.content}</ReactMarkdown>
                            </div>
                            {step.benefit && <p className="mt-3 text-sm text-blue-300 bg-blue-900/50 p-3 rounded-md ring-1 ring-inset ring-blue-500/20"><strong className="font-semibold text-blue-200">Benefit:</strong> {step.benefit}</p>}
                            {step.practical_focus && <p className="mt-3 text-sm text-green-300 bg-green-900/50 p-3 rounded-md ring-1 ring-inset ring-green-500/20"><strong className="font-semibold text-green-200">Action:</strong> {step.practical_focus}</p>}
                        </li>
                    ))}
                </ol>
            </Card>
        ))}

        <Card title="Explanation and Kickstart Examples" icon={<SparklesIcon />}>
            {pathway.explanation_and_kickstart_examples.map((exp, index) => (
                <div key={index} className="pb-4 mb-4 border-b border-slate-700 last:border-b-0">
                    <h4 className="font-bold text-lg text-white">{exp.title}</h4>
                    <div className="mt-2 markdown-content">
                        <ReactMarkdown>{exp.content}</ReactMarkdown>
                    </div>
                </div>
            ))}
        </Card>

        <Card title="History and Milestones" icon={<HistoryIcon />}>
            <ul className="space-y-3">
                {pathway.history_and_milestones.map((milestone, index) => (
                    <li key={index} className="flex items-start gap-3">
                        <CheckIcon />
                        <div>
                           <strong className="font-semibold text-white">{milestone.year}:</strong> {milestone.description}
                        </div>
                    </li>
                ))}
            </ul>
        </Card>

        <Card title={pathway.next_steps.title} icon={<NextIcon />}>
             <ul className="space-y-4">
                {pathway.next_steps.steps.map((step, index) => (
                    <li key={index} className="p-3 bg-slate-900/30 rounded-md border border-slate-700">
                        <h4 className="font-semibold text-white">{step.title}</h4>
                        <p className="text-slate-300">{step.description}</p>
                    </li>
                ))}
            </ul>
        </Card>

        <Card title="Relevant Links" icon={<LinkIcon />}>
            <ul className="space-y-2">
                {pathway.relevant_links.map((link, index) => (
                    <li key={index}>
                        <a href={link} target="_blank" rel="noopener noreferrer" className="text-blue-400 hover:text-blue-300 hover:underline break-all flex items-center gap-2">
                           <ArrowIcon /> {link}
                        </a>
                    </li>
                ))}
            </ul>
        </Card>

        <div className="text-center mt-12">
            <button
                onClick={onTryAgain}
                className="bg-gradient-to-r from-blue-600 to-purple-600 text-white font-bold py-3 px-8 rounded-lg shadow-lg hover:from-blue-500 hover:to-purple-500 focus:outline-none focus:ring-4 focus:ring-blue-400/50 transition-all transform hover:scale-[1.02] hover:shadow-[0_0_20px_rgba(96,165,250,0.5)]"
            >
                Create Another Pathway
            </button>
        </div>
    </div>
  );
};

export default PathwayDisplay;