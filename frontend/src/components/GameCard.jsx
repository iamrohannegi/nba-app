import styles from './GameCard.module.css';

const GameCard = (props) => {
    return (
        <div>
            <h3>{props.name}</h3>
            { Object.entries(props.ratings).map(([ratingName, rating]) => {
              return (
                <ul key={`${props.id}/${ratingName}`}>
                  <li>{ ratingName } : { rating }</li>
                </ul>
            )})}
        </div>
    );
};

export default GameCard