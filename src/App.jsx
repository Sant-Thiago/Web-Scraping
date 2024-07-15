import './App.css';
import Input from './components/Input';

function App() {

  return (
    <div className='containerApp'>
      <h1>Web Scraping</h1>
      <form action="/" method="post">
        <Input />
      </form>
      <div id='result'></div>
    </div>
  );
}

export default App;
