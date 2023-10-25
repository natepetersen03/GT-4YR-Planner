import logo from './logo.svg';
import './App.css';
import {useState, useEffect} from 'react';

function App() {
  const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            const response = await fetch('http://localhost:5000/schedule')
            const newData = await response.json()
            setData(newData)
        };

        fetchData();
    }, [])

    if (data) {
        console.log(data)
        return <div className='App'>{data.name}</div>;
    } else {
        return null;
    }
}

export default App;
