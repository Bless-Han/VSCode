#include <stdio.h>
#define MAXN 100001

int k, result, thisSum, maxSum;
int a[MAXN];

void init();
int alg2();
int alg3(int left, int right);
int alg4();
int max(int a, int b);
int main(void){
  init();
  // result = alg2();
  // result = alg3(0, k-1);
  result = alg4();
  printf("%d\n", result);
  return 0;
}

void init(){
  k=result=thisSum=maxSum=0;
  scanf("%d", &k);
  for (int i=0; i<k; i++){
    scanf("%d", &a[i]);
  }
}
int alg2(){
  for (int i=0; i<k; i++){
    for (int j=i; j<k; j++){
      thisSum += a[j];
      if (thisSum > maxSum){
        maxSum = thisSum;
      }
    }
    thisSum = 0;
  }
  return maxSum;
}
int alg3(int left, int right){
	//递归出口 ,当只有一个元素的时候，大于0的将其返回，否则返回0 
	if(left==right)
	{
		if(a[left]>0)
		return a[left];
		else 
		return 0;
	}
	int mid=(left+right)/2;//找到中点 
	
	//分的过程 
	int maxLeft =   alg3(left,mid);
	int maxRight = alg3(mid+1,right);
	
    //求跨界，该子列包括 a[mid],所以由mid为中心向两边求跨界的最大子列和 
	int borderLeft=0;
	int borderRight=0;
	int sumLeft =0;
	int sumRight=0;
	
	//由中点mid向左扫描 
	for(int i=mid;i>=left;i--){
		borderLeft+=a[i];
		if(borderLeft>sumLeft)//向左更新左边最大子列和 
		sumLeft=borderLeft; 
	} 
	//由中点mid向右扫描
	for(int i=mid+1;i<=right;i++){
		borderRight+=a[i];
		if(borderRight>sumRight)//向右更新右边的最大子列和 
		sumRight=borderRight;
	} 
	// sumRight+sumLeft为该范围跨界的最大子列和
	//maxLeft为left到mid范围内的最大子列和
	//maxRight为mid+1到right的最大子列和 
	//返回三者的最大值 
	return max(max(maxLeft,maxRight),sumRight+sumLeft);
}
int alg4(){
  for (int i=0; i<k; i++){
    thisSum += a[i];
    if (thisSum < 0)
      thisSum = 0;
    if (thisSum > maxSum)
      maxSum = thisSum;
  }
  return maxSum;
}
int max(int a, int b){
  return a>b?a:b;
}
