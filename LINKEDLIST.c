#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
	struct node{
		int data;
		int key;
		struct node *next;
	};
	struct node *head=NULL;
	struct node *current=NULL;
	void printlist(){
		struct node *ptr=head;
		printf("\n[ ");
		while(ptr!=NULL){
			printf("(%d,%d)",ptr->key,ptr->data);
			ptr=ptr->next;
		}
		printf(" ]");
		
	}
	//add an element at first
	void insertFirst(int key,int data){
		struct node *link=(struct node*) malloc(sizeof(struct node));
		link->key=key;
		link->data=data;
		link->next=head;
		head=link;
	}
	//delete the first element
	struct node* deleteFirst(){
		struct node *templink=head;
		head=head->next;
		return templink;
	}
	//check if list is empty
	bool isempty(){
		return head==NULL;
	}
	//check length of list
	int length(){
		int length = 0;
		struct node* current;
		for(current=head;current!=NULL;current=current->next){
			length++;
		}
		return length;
	}
	//check if element exist
	struct node* find(int key){
		struct node *current=head;
		if(head==NULL){
			return NULL;
		}
		while(current->key!=key){
			if(current->next=NULL){
				return NULL;
			}
			else{
				current=current->next;
			}
		}
		return current;
	}
	//delete the link for specific key
	struct node* delete(int key){
		struct node *current=head;
		struct node *previous=NULL;
		if(head==NULL){
			return NULL;
		}
		while(current->key!=key){
			if(current->next==NULL){
				return NULL;
			}
			else{
				previous=current;
			current=current->next;
			}
		}
		if(current==head){
			head=head->next;
		}
		else{
			previous->next=current->next;
		}
		return current;
	}
	//sort the list
	void sort(){
 		int i, j, k, tempKey, tempData ;
 		struct node *current;
 		struct node *next;
 		int size = length();
 		k = size ;
 		for ( i = 0 ; i < size - 1 ; i++, k-- ) {
 			current = head ;
			next = head->next ;
			for ( j = 1 ; j < k ; j++ ) { 
 				if ( current->data > next->data ) {
 				tempData = current->data ;
 				current->data = next->data;
 				next->data = tempData ;
 				tempKey = current->key;
 				current->key = next->key;
 				next->key = tempKey;
 			}
 		current = current->next;
 		next = next->next;
 			}
 		}
	}
int main(){
	insertFirst(1,102);
	insertFirst(2,112);
	insertFirst(3,12);
	insertFirst(4,44);
	printlist();
	sort();
	printlist();
	return 0;
}
