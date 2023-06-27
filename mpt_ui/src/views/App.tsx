import React, {useState} from "react";
import axios, {AxiosResponse} from "axios";
import './App.css';


type AppHeaderContainerProps = {
	children: React.ReactNode;
}

const AppHeaderContainer: React.FC<AppHeaderContainerProps> = (props) => {
	// ヘッダーの枠
	return (
		<div className="App-header">
			{props.children}
		</div>
	);
}

type AppHeaderProps = {
	title: string;
}


const Title: React.FC<AppHeaderProps> = (props) => {
	// タイトル(ロゴになる)
	return (
		<div>{props.title}</div>
	);
}

// コンテンツの枠
type ContentsContainerProps = {
	children: React.ReactNode;
}

const ContentsContainer: React.FC<ContentsContainerProps> = (props) => {
	return (
		<div className="App-Contents">
			{props.children}
		</div>
	)
}

function App() {
	return (
		<div>
			<AppHeaderContainer>
				<Title title="Math Problems Tutor"/>
			</AppHeaderContainer>
			<ContentsContainer>
			</ContentsContainer>
		</div>
	)
}

export default App;
