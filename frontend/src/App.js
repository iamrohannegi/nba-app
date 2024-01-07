import { useState, useEffect } from 'react';
import './App.css';

const baseUrl = "http://localhost:5000/games/"
let firstLoad = true

function App() {
  const [games, setGames] = useState(null)

  useEffect(() => {
    if ( firstLoad ) {
      const yesterday = new Date()
      yesterday.setDate(yesterday.getDate() - 1)      
      const formattedDate = `${yesterday.getFullYear()}${(yesterday.getMonth()+1).toString().padStart(2, 0)}${yesterday.getDate().toString().padStart(2, 0)}`
      const fetchingData = async () => {
        // const res = await fetch(`${baseUrl}${formattedDate}`)
        const res = await fetch(`${baseUrl}20240103`)
        console.log(res)
        const data = await res.json()
        console.log(data)
        setGames(data)
      }

      fetchingData()
      firstLoad = false
    }
  }, [])

  return (
    <div className="App">
      <p>Hello</p>
      <button>Click to get results</button>
      { !games && <p>Loading...</p>}
      { games && <p>Games Loaded </p>}
      { games && Object.entries(games).map(([gameName, gameData]) => {
        return (
          <div key={gameData.id}>
            <h2>{ gameName }</h2>
            <p>Rating: </p>
            { Object.entries(gameData['ratings']).map(([ratingName, rating]) => {
              return (
                <ul key={`${gameData.id}/${ratingName}`}>
                  <li>{ ratingName } : { rating }</li>
                </ul>
            )})}
          </div>
      )})}
    </div>
  );
}

export default App;
