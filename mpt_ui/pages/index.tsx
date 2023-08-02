import React from 'react';
import Head from 'next/head';
import {NextPage} from 'next';
import './index.css';
import Page from 'components/Page';

const AllProblemPage : NextPage = () => {
	const units: string[] = [];
	for (let i = 0; i < 25; i++) {
		units.push('Unit' + (i).toString());
	}
	return (
		<Page>
            {units.map((unit) => (
                <div className="App-Unit-Box">
                    <div className="App-Unit-Text-Frame">
                        <p className="App-Unit-Text">{unit}</p>
                    </div>
                </div>
            ))}
		</Page>
	)
}

export default AllProblemPage;