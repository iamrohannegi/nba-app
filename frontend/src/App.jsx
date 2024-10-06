import { useState, useEffect, useRef } from 'react';
import './App.css';

import ScoreContext from './store/score-context';
import CardsContainer from './components/CardsContainer';
import Header from './components/Header';
import Container from './components/Container';

const baseUrl = "https://nba-game-rating.onrender.com/games/"
// const baseUrl = "http://localhost:5000/games/"
let firstLoad = true

function App() {
  const [isScoreVisible, setIsScoreVisible] = useState(false)
  const [games, setGames] = useState(null)
  const [topGames, setTopGames] = useState(null)
  const [dateGames, setDateGames] = useState(null)
  const [loading, setLoading] = useState(false);
  const dateRef = useRef(null);

  const handleScoreVisibilityChange = (visible) => { 
    setIsScoreVisible(visible)
  }

  useEffect(() => {
    if ( firstLoad ) {
      const yesterday = new Date()
      yesterday.setDate(yesterday.getDate() - 1)      
      let formattedDate = `${yesterday.getFullYear()}${(yesterday.getMonth()+1).toString().padStart(2, 0)}${yesterday.getDate().toString().padStart(2, 0)}`
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

  const handleSeachClick = async () => {
    const value = dateRef.current.value.trim();
    
    if (!value) {
      return;
    }

    setLoading(true);
    const formattedDate = value.split("-").join(""); 
    const res = await fetch(`${baseUrl}${formattedDate}`);
    const data = await res.json();
    setDateGames(data);
    setLoading(false);
  };

  return (
    <ScoreContext.Provider value={{ isScoreVisible: isScoreVisible, handleScoreVisibilityChange: handleScoreVisibilityChange}}>
      <Header/>
      <Container>
        <h2 className="section-heading">Yesterday's Games</h2>
        { !games && <p className="grey-centered-text">Loading...</p>}
        { games && Object.keys(games).length <= 0 && <p className="grey-centered-text">No games were played yesterday.</p>}
        { games && <CardsContainer cards={games} />}

        <h2 className="section-heading">Top picks from last 5 days</h2>
        { !topGames && <p className="grey-centered-text">Loading...</p>}
        { topGames && Object.keys(topGames).length <= 0 && <p className="grey-centered-text">No games were played in the last 5 days</p>}
        { topGames && <CardsContainer cards={topGames} />}

        <h2 className="section-heading">Search Game Ratings by Date </h2>
        <div className="search-div">
          <label>Choose a date: <input type="date" ref={dateRef}/></label>
          <button onClick={handleSeachClick}>Search</button>
        </div>
        { loading && <p className="grey-centered-text">Loading...</p>}
        { !loading && !dateGames && <p className="grey-centered-text">Search for a specific date</p>}
        { !loading && dateGames && Object.keys(dateGames).length <= 0 && <p className="grey-centered-text">Could not find any games</p>}
        { dateGames && <CardsContainer cards={dateGames} />}
      
      </Container>
    </ScoreContext.Provider>
  );
}

export default App;
