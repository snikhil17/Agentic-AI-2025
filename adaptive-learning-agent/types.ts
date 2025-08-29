
export interface LearningPreferences {
  learningStyle: string;
  topic: string;
  hobbies: string;
  domain: string;
  googleApiKey: string;
  tavilyApiKey: string;
}

export interface PathwayPhase {
  title: string;
  description: string;
  steps: {
    title: string;
    type: 'concept' | 'example' | 'project' | 'resource';
    content: string;
    benefit?: string;
    practical_focus?: string;
  }[];
}

export interface ExplanationSection {
  title: string;
  content: string;
}

export interface Milestone {
  year: number;
  description: string;
}

export interface NextStepsSection {
  title: string;
  steps: {
    title: string;
    description: string;
  }[];
}

export interface LearningPathway {
  title: string;
  introduction: string;
  phases: PathwayPhase[];
  explanation_and_kickstart_examples: ExplanationSection[];
  history_and_milestones: Milestone[];
  next_steps: NextStepsSection;
  relevant_links: string[];
}
