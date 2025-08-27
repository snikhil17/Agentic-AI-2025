import React from 'react';

export const Footer: React.FC = () => (
  <footer className="py-6 mt-auto text-center text-slate-400">
    <p>&copy; {new Date().getFullYear()} Adaptive Learning Agent. All rights reserved.</p>
  </footer>
);