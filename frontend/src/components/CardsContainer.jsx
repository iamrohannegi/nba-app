import styles from './CardsContainer.module.css'

import GameCard from './GameCard';

const CardsContainer = (props) => {
    return (
        <section className={styles.container}>
            {Object.entries(props.cards).map(([gameName, gameData]) => {
                return (
                    <GameCard key={gameData.id} id={gameData.id} name={gameName} ratings={gameData['ratings']} teams={gameData.teams}/>
                )
            })}
        </section>
    )
};

export default CardsContainer;