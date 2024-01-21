import styles from './CardsContainer.module.css'

import GameCard from './GameCard';

const CardsContainer = (props) => {
    return (
        <section className={styles.container}>
            {Object.entries(props.cards).map(([idx, gameData]) => {
                return (
                    <GameCard 
                        key={gameData.id} 
                        id={gameData.id} 
                        name={gameData.name} 
                        teams={gameData.teams}
                        ratings={gameData.ratings} 
                        overall_rating={gameData.overall_rating}
                    />
                )
            })}
        </section>
    )
};

export default CardsContainer;