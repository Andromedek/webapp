# webapp application 


1- What would you do differently on a managed cluster (EKS, GKE...) regarding step 4?
response : 

2. How would you monitor the application?
response: 
Since I am using Kind the better way is to include metric api and using kubectl top. 
for a sample cluster one master node : 
download this :
> kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
then use kubectl top pod webapp

3. What would you change to add a PostgreSQL container?
I would add storage volume. 

4. Provide us some feedback on this test:
a. Duration: is it too long, too short or adequate? adequate.

b. Difficulty: on a scale from 0 (easy) to 10 (hard), how would you rate the difficulty
of this test?  5

c. Did you find the test interesting? If not, please tell us why.
  Yes, that would be useful if we could have a specific git repository and manage a preconfigured webapp code. 
