import { useState, useEffect } from 'react';
import './App.css';

import ScoreContext from './store/score-context';
import CardsContainer from './components/CardsContainer';
import Header from './components/Header';
import Container from './components/Container';

const baseUrl = "https://nba-game-rating.onrender.com/games/"
let firstLoad = true

function App() {
  const [isScoreVisible, setIsScoreVisible] = useState(false)
  const [games, setGames] = useState(null)
  const [topGames, setTopGames] = useState(null)

  const handleScoreVisibilityChange = (visible) => { 
    setIsScoreVisible(visible)
  }

  useEffect(() => {
    if ( firstLoad ) {
      const yesterday = new Date()
      yesterday.setDate(yesterday.getDate() - 1)      
      const formattedDate = `${yesterday.getFullYear()}${(yesterday.getMonth()+1).toString().padStart(2, 0)}${yesterday.getDate().toString().padStart(2, 0)}`

      const fetchingYesterdaysGames = async () => {
        // const res = await fetch(`${baseUrl}${formattedDate}`)
        const res = await fetch(`${baseUrl}${formattedDate}`)
        console.log(res)
        const data = await res.json()
        console.log(data)
        setGames(data)
      }

      const fetchingTopGames = async () => {
        // const res = await fetch(`${baseUrl}${formattedDate}`)
        const res = await fetch(`${baseUrl}top`)
        console.log(res)
        const data = await res.json()
        console.log(data)
        setTopGames(data)
      }

      const fetchGames = async () => {
        await fetchingYesterdaysGames()
        await fetchingTopGames()
      }

      fetchGames()
      firstLoad = false
    }
  }, [])

  return (
    <ScoreContext.Provider value={{ isScoreVisible: isScoreVisible, handleScoreVisibilityChange: handleScoreVisibilityChange}}>
      <Header/>
      <Container>
        <h2 className="section-heading">Yesterday's Games</h2>
        { !games && <p>Loading...</p>}
        { games && <CardsContainer cards={games} />}

        <h2 className="section-heading">Top picks from last 5 days</h2>
        { !topGames && <p>Loading...</p>}
        { topGames && <CardsContainer cards={topGames} />}
      </Container>
    </ScoreContext.Provider>
  );
}

export default App;
