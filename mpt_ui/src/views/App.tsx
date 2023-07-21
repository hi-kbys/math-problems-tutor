import React, {useState} from "react";
import axios, {AxiosResponse} from "axios";
import './App.css';


type AppHeaderContainerProps = {
	children: React.ReactNode;
}

const AppHeaderContainer: React.FC<AppHeaderContainerProps> = (props) => {
	// ヘッダーの枠
	return (
		<header className="App-header">
			{props.children}
		</header>
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

type ContentsFrameProps = {
	children: React.ReactNode;
}

// コンテンツの背景
const ContentsFrame: React.FC<ContentsFrameProps> = (props) => {
	return (
		<div className="App-Contents-Frame">
			{props.children}
		</div>
	)
}

function App() {
	const units: string[] = [];
	for (let i = 0; i < 25; i++) {
		units.push('Unit' + (i).toString());
	}
	return (
		<ContentsContainer>
			<AppHeaderContainer>
				<Title title="Math Problems Tutor"/>
			</AppHeaderContainer>
			<ContentsFrame>
				{units.map((unit) => (
					<div className="App-Unit-Box">
						<div className="App-Unit-Text-Frame">
							<p className="App-Unit-Text">{unit}</p>
						</div>
					</div>
				))}
			</ContentsFrame>
		</ContentsContainer>
	)
}

export default App;
