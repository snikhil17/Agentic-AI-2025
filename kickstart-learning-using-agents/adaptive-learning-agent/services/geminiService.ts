
import type { LearningPreferences, LearningPathway } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000';

export const generateLearningPathway = async (preferences: LearningPreferences): Promise<LearningPathway> => {
    try {
        const response = await fetch(`${API_BASE_URL}/api/generate-pathway`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(preferences),
        });

        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
        }

        const pathwayData = await response.json();
        return pathwayData as LearningPathway;
    } catch (error) {
        console.error("Error generating learning pathway from backend:", error);
        if (error instanceof Error) {
            throw new Error(`Failed to generate learning pathway: ${error.message}`);
        } else {
            throw new Error("Failed to generate learning pathway. Please check your connection and try again.");
        }
    }
};
