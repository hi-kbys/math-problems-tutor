import React from 'react';
import {NextPage} from 'next';
import index from './index.module.css';
import Page from 'components/Page';

const AllProblemPage : NextPage = () => {
	const units: string[] = [];
	for (let i = 0; i < 25; i++) {
		units.push('Unit' + (i).toString());
	}
	return (
		<Page>
            {units.map((unit) => (
                <div className={index.App_Unit_Box} key={unit}>
                    <div className={index.App_Unit_Text_Frame}>
                        <p className={index.App_Unit_Text}>{unit}</p>
                    </div>
                </div>
            ))}
		</Page>
	)
}

export default AllProblemPage;
