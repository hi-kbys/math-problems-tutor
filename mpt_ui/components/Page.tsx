import React from 'react';
import Head from 'next/head';
import {NextPage} from 'next';
import './Page.css';
import { getImgProps } from 'next/dist/shared/lib/get-img-props';


type HeaderProps = {
    title: string;
}

const Header: React.FC<HeaderProps> = (props) => {
	// ヘッダーの枠
	return (
		<header className="App-header">
			<div>{props.title}</div>
			<div>Githubアイコン（予定）</div>
		</header>
	);
}

// コンテンツの枠
type ContentsContainerProps = {
	children: React.ReactNode;
}

const ContentsContainer: React.FC<ContentsContainerProps> = (props) => {
	return (
		<div className="App-Contents">
            <div className="App-Contents-Frame">
			    {props.children}
		    </div>
		</div>
	)
}

type PageProps = {
    children: React.ReactNode;
}
const Page: NextPage<PageProps> = (props) => {
    return (
        <>
        <Head>
            <title>My page title</title>
        </Head>
        <Header title="Math Problems Tutor"/>
        <ContentsContainer>
            {props.children}
		</ContentsContainer>
        </>
    );

}
export default Page
