import React from 'react';

const ScoreContext =  React.createContext({
    isScoreVisible: false,
    handleScoreVisibilityChange: () => {}
});

export default ScoreContext;
