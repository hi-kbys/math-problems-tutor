import React, {useState, useEffect, FormEvent} from 'react';
import {NextPage} from 'next';
import problems from './problems.module.css';
import Page from 'components/Page';

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
		<div className={problems.Problem_Frame}>
			<div>問題1</div>
			<div className="Problem-Frame-Contents">{problemStatement}</div>
		</div>
	)
}


// 送信後の挙動

// chatの取得

// 質問の枠

const QAFrame: React.FC = () => {
	// 質問は動的に増えるので、配列で管理する
	const exampleQAList: string[] = ["ほげがわかりません", "ふがはいかがでしょう", "ぴよについて教えて"];
	const [chats, setChats] = useState<string[]>(exampleQAList);
	console.log(chats);

	const [message, setMessage] = useState<string>("");

	// 送信ボタンを押したときの挙動
	const sendMessage = async (e: FormEvent<HTMLFormElement>) => {
		e.preventDefault();
		setChats([...chats, message]);
		setMessage("");
	}
	
	// 表示前に一度だけ質問を取得する
	useEffect(() => {
		return () => {
			
		}
	}, [])


	return (
		<div className={problems.Question_Frame}>
			{chats.map((message) => (
				<div className="Question-Frame-Contents">{message}</div>
			))}
			<div className={problems.Send_Message_Form}>
				<form onSubmit={sendMessage}>
					<input type="text" value={message} onChange={(e) => setMessage(e.target.value)} />
					<input type="submit" value="送信" />
				</form>
			</div>
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
