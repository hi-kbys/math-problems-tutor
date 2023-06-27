import React, {useState} from "react";
import axios, {AxiosResponse} from "axios";

type Hello = {
  Hello: string;
}

// ヘッダーの実装
const Header: React.FC = () => {
	return (
		<div>
			<h1>ヘッダー</h1>
		</div>
	);
}

function App() {
	const [data, setData] = useState<Hello>();
	const url: string = "http://127.0.0.1:8000";

	const GetData = () => {
		axios.get(url).then((res: AxiosResponse<Hello>) => {
			setData(res.data);
		});
	};
	return (
		<div>
			<div>ここに処理を書いていきます</div>
			{data ? <div>{data.Hello}</div> : <button onClick={GetData}>データを取得</button>}
		</div>
	);
}

export default App;
