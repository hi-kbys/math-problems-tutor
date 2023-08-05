import React from 'react';
import Head from 'next/head';
import Link from 'next/link';
import {NextPage} from 'next';
import page from './Page.module.css';
import { getImgProps } from 'next/dist/shared/lib/get-img-props';


type HeaderProps = {
    title: string;
}

const Header: React.FC<HeaderProps> = (props) => {

	// ヘッダーの枠
	return (
		<header className={page.App_header}>
			<div>{props.title}</div>
			<Link href="https://github.com/abist-kobayashi/math-problems-tutor" passHref>
				<img src="github.svg" alt="github" />
      		</Link>
			
		</header>
	);
}

// コンテンツの枠
type ContentsContainerProps = {
	children: React.ReactNode;
}

const ContentsContainer: React.FC<ContentsContainerProps> = (props) => {
	return (
		<div className={page.App_Contents}>
            <div className={page.App_Contents_Frame}>
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
