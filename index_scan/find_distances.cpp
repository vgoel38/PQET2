#include<stdio.h>
#include<iostream>
#include<map>
#include<algorithm>
#include<list>

using namespace std;

#define num_tuples 36244344
#define num_pages 288333+10

long long int total_rounds = 0;

long long int find_distanc(long long int x, long long int y){
	//going from x to y
	if(x<y) total_rounds++;
	return x-y;
}

long long int present[num_pages],distanc[num_tuples],page_id[num_tuples],total_full_rounds[num_tuples];

int main(){

	freopen("page_ids.csv","r",stdin);
	freopen("distancs.csv","w",stdout);

	// int num_tuples=36244344,x,num_pages=288333+10;

	for(int i=0;i<num_tuples;i++) cin>>page_id[i];
	for(int i=0;i<num_pages;i++) present[i]=0;
	long long int last_page=page_id[0];
	present[page_id[0]]=1;
	distanc[0]=0;

	for(int i=1;i<num_tuples;i++){
		distanc[i]=distanc[i-1];
		total_full_rounds[i]=total_rounds;
		if(!present[page_id[i]]){
			present[page_id[i]]=1;
			distanc[i]+=find_distanc(last_page,page_id[i]);
			last_page=page_id[i];
			total_full_rounds[i]=total_rounds;
		}
	}

	for(int i=0;i<num_tuples;i++) cout<<distanc[i]<<"\n";
	
	freopen("rounds.csv","w",stdout);
	for(int i=0;i<num_tuples;i++) cout<<total_full_rounds[i]<<"\n";
   	
	return 0;
}