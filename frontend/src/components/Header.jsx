import styles from './Header.module.css';
import Container from './Container';

const Header = () => {
    return (
        <header className={styles.header}>
            <Container>
                <h2 className={styles.heading}>NBA Ratings <span>- A spoiler-free site to save your time </span></h2>
            </Container>
        </header>        
    )
}

export default Header;