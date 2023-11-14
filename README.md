# How to collaborate
1. clone repository
```
git clone https://github.com/Ayshyama/forTutoring
```
2. check remote
```
git remote -v
```
3. if remote is not Ayshyama/forTutoring, then add remote
```
git remote add origin https://github.com/Ayshyama/forTutoring.git
```

# If you want to have the same repository inside your Git account, you can fork it.

- When you fork a project, you essentially create a copy of the original (upstream) repository under your own GitHub account. 
- This gives you full control over your forked repository, and you can push updates to it as you wish. 

## Working with forks:

### Two Remote Repositories

- Origin: This is your forked repository. When you clone your fork to your local machine, 
- Git automatically names this remote "origin".

- Upstream: This is the original repository that you forked. 
- Generally, you would add this as a second remote named "upstream" to pull in changes from the original project.

## Pulling Updates from the Original Repository(Upstream)

1. Navigate to Local Repository: Open your terminal and navigate to the directory of your local Git repository.
2. Add Upstream Remote: If you haven't already added the original repository as an "upstream" remote, you can do so with:
```
git remote add upstream https://github.com/original_owner/original_repository.git
```
or ssh
```
git remote add upstream git@github.com:original_owner/original_repository.git
```
3. verify remote (you should see origin and upstream) 
```
git remote -v
```
4. Fetch and Merge Changes from Upstream (original repo)
- Fetch will only download the changes from the upstream repository, but not merge them with your local commits.
- Before pushing new changes, it's often good to fetch and merge changes from the "upstream" repository so that your fork stays up-to-date.
```
git fetch upstream
```
5. Checkout Branch: Make sure you are on the branch into which you want to merge the updates.
```
git branch
```
```
git checkout branch_name
```
6. Merge Changes: Merge the changes from the upstream repository's main branch into your local main branch.
```
git merge upstream/branch_name
```
7. Push to Your Fork: Finally, push these merged changes to your own forked repository on GitHub.
- Push Changes to Your Fork: After resolving any conflicts and committing your changes, you can push to your fork.
```
git push origin main
```

## Pulling Updates from Your Fork (Origin)
1. Navigate to Local Repository: Open your terminal and navigate to the directory of your local Git repository.
2. Checkout Branch: Make sure you are on the branch into which you want to merge the updates.
```
git checkout branch_name
```
3. Pull updates from your fork
```
git pull origin branch_name
```

### If you have set wrong remote origin or upstream follow these steps:
- to change remote origin
```
git remote set-url origin https://github.com/username/repository.git
```
- to change remote upstream
```
git remote set-url upstream https://github.com/username/repository.git
```

## Here's how you can manage where to push your updates:
- You generally can't push to upstream unless you are an authorized contributor.
- So, you can push to your fork: git push origin <branch_name>.
- Or ask for permission to push to upstream.
- Or create a pull request to propose changes to the upstream project.
- Most often, you'll be pushing to your own fork and then creating a pull request to propose changes to the upstream project.

## Decide Where to Push: Now you have two remotes: "origin" and "upstream".
- Push to your fork: git push origin <branch_name>
- You generally can't push to upstream unless you are an authorized contributor.

- Push to your fork: 
```
git push origin <branch_name>
```

- Push to upstream: 
```
git push upstream <branch_name>
```
- Fetch and Merge Changes from Upstream: Before pushing new changes, 
- it's often good to fetch and merge changes from the "upstream" repository so that your fork stays up-to-date.





### When working with branches and collaborative efforts in Git, especially with multiple people making changes to the same files, there are a few common strategies to manage the workflow efficiently and avoid conflicts:

- Feature Branch Workflow:
Each developer works on a separate branch for each feature or component they are developing. In your case, one person could create a branch feature/user-model, and the other could create feature/product-warehouse-model. This way, they can work in parallel without interfering with each other's work.

- Pull Before You Push:
If they must work on the same branch (like 'Models'), it's good practice to always pull the latest changes from the 'Models' branch before starting work and also right before pushing. This minimizes the chances of conflicts.

- Resolve Conflicts Locally:
If there are any conflicts after pulling the latest changes, they should be resolved locally on the developer's machine before pushing the changes back to the remote branch.

- Small and Frequent Commits:
Developers should commit changes frequently and push them to the remote branch often. This helps to reduce the scope of conflicts and makes them easier to resolve.

- Communication:
Communication is key in a collaborative environment. Developers should inform each other when they are about to push changes or if they will be making changes that could affect the other person's work.

- Code Reviews:
Before merging the 'Models' branch back into the main branch, it's good practice to have a code review process where other team members review the changes for any issues or conflicts.

- Pull Requests:
Developers should use pull requests to merge their feature branches back into the 'Models' branch. This provides an opportunity for other team members to review the changes and ensure that they integrate well with the existing codebase.

- Continuous Integration (CI):
If available, use a CI system to automatically test the changes when pushed to a shared branch to ensure they don't break the build or existing functionality.


### Imagine a task:
```
*Model Creation*
 - Create User, Product, and Warehouse models.
*Dev1 should create User model*
*Dev2 should create Product model*
*Dev3 should create Warehouse model*
 - User: Use Django's built-in User model.
 - Product: Include relevant fields and a ForeignKey to the Warehouse model.
 - Warehouse: Define fields like location, capacity, etc.
```

The recommended approach would be for each person to create their own *feature branch* from 'Model Creation' (for example a branch 'user_model_creation'), do their work, and then merge or rebase their *feature branch* onto the updated 'Models Creation' branch before submitting a pull request.
This allows them to work in parallel and reduces the likelihood of stepping on each other's toes. 
It also makes the process of integrating changes smoother and more controlled.

If two people are working on different files, they can technically work on the same branch and commit their changes independently without much risk of conflict. 
However, it's still a good practice to frequently pull changes from the remote branch to ensure that each developer's local copy is up to date.

In summary, using feature branches, pulling often, communicating with team members, and making frequent small commits can help avoid conflicts and streamline the development process when multiple people are working on the same project.
