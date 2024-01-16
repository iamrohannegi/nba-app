import styles from './Header.module.css';

const Header = () => {
    return (
        <header className={styles.header}>
            <h2 className={styles.heading}>NBA Ratings <span>- A spoiler-free site to save your time </span></h2>
        </header>        
    )
}

export default Header;