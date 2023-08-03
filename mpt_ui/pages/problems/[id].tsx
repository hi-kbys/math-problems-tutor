import React, {useState, useEffect, use} from 'react';
import Head from 'next/head';
import {NextPage} from 'next';
import './problems.css';
import Page from 'components/Page';
import { userAgent } from 'next/server';

// 問題の枠
const ProblemFrame: React.FC = () => {
	let exampleProblemStatement: string = "1枚ずつのカードに「h」、「e」、「l」、「l」、「o」と書かれた5枚のカードを並べていきます。 \
	\
	(1)両はしが「l」になる並び方は全部で何通りありますか。 \
	(2)「l」がとなりあう並び方は全部で何通りありますか。\
	(3)左はしが「e」になる並び方は全部で何通りありますか。";
	const [problemStatement, setProblemStatement] = useState<string>(exampleProblemStatement)

	// 表示前に一度だけ問題文を取得する
	useEffect(() => {
		return () => {
		}
	}, [problemStatement])

	return (
		<div className="Problem-Frame">
			<div className="Problem-Frame-Title">問題1</div>
			<div className="Problem-Frame-Contents">{problemStatement}</div>
		</div>
	)
}

// 質問の枠
const QAFrame: React.FC = () => {
	// 質問は動的に増えるので、配列で管理する
	const exampleQAList: string[] = ["ほげがわかりません", "ふがはいかがでしょう", "ぴよについて教えて"];

	const [chats, setChats] = useState<string[]>(exampleQAList);

	// 表示前に一度だけ質問を取得する
	useEffect(() => {
		return () => {
			
		}
	}, [chats])

	return (
		<div className="Question-Frame">
			{chats.map((message) => (
				<div className="Question-Frame-Contents">{message}</div>
			))}
		</div>
	)
}

const ProblemPage : NextPage = () => {


	// 問題の枠
	return (
		<Page>
			<ProblemFrame></ProblemFrame>
			<QAFrame></QAFrame>
		</Page>
	)
}

export default ProblemPage;
