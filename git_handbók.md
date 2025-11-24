Hvað er Git?
-	Git er vefþjónusta sem gerir notendum kleyft að geyma, deila og vinna saman að kóða
-	Notum git til að:
o	Fylgjast með hvaða breytingar hver og einn gerir í skrám
o	Vinna með branches til að vera ekki að breyta aðalkóðanum fyrr en við erum viss um allt sé rétt, áður en kóðanum er push-að í aðalkóðann
o	Deila kóða með teymi/hóp til að vinna á skipulagðan hátt
-	Fyrst þarf einn úr hópnum að búa til repository
o	Deilir því með meðlimum sem clone-a það á sitt github desktop app til að geta unnið með repo-ið á sinni tölvu og ýtt sínum kóða í það

Git skipanir
-	Setjum git fyrir framan skipunina
Repo = repository
Branch
-	A copy of the project used for working in an isolated environment without affecting the main project
-	Git flow er ákveðin aðferðarfræði við það að búa til branches
o	Main – alltaf nýjasta útgáfan af kóðanum með öllu réttu
o	Develop – þar sem nýr kóði er þróaður
o	Feature branches - fyrir nýja virkni
o	Release branches – til að undirbúa nýja útgáfu
o	Hotfix branches – til að laga alvarlegar villur í kóðanum
o	Hjálpar til við að halda skipulagi í stórum erkefnum

Clone
-	The act of making a clone or a copy of a repository in a new directory
Git init (býr til nýtt git repo)
-	Býr til nýtt Git repo í ákveðinni möppu. 
-	Ef skipunin er keyrð í möppu sem inniheldur nú þegar verkefni, þá býr hún til Git repo í þeirr möppu
Git add . (bætir skrám í möppu)
-	Setur allar breytingar í núverandi möppu í “undirbúnings” þannig að þær verði tilbúnar fyrir næsta commit
-	Stages all changes in the current directory to the next commit
-	Punkturinn þýðir að allar skrár og allar undirmöppur í núverandi möppu eru teknar með
Git commit -m “initial commit” 
-	Staðfestir (commit-ar) skrárnar sem hafa verið bætt við með git add. 
-	Flaggið -m gerir okkur kleyft að bæta strax við skilaboðum fyrir commit-ið (“initial commit” er þá skilaboðin fyrir commit-ið)
Git Push (ýta breytingum á GitHub)
-	Ýtir öllum local commits í remote reposotory (mappan í Git skýjinu)
Git Push -u origin master
-	Flaggið -u setur “upstream branch” sem þýðir að við þurfum ekki að skilgreina aftur hvaða grein (branch) þegar maður notar git push
Git checkout -b <branch_name>
-	Býr til nýja grein (branch) og skiptir yfir í hana í einu skrefi
Git checkout <branch_name>
-	Skiptir yfir á tiltekna grein (branch)
-	Getum aðeins unnið í einni grein í einu
Git merge <source_branch>
-	Sameinar tiltekna grein inn í þá grein sem þú ert nú þegar á.
Git status
-	Sýnir stöðu breytinga 
o	Hvort að skrár eru untracked, modified eða staged
-	Gefur yfirlit yfir núverandi stöðu í möppunni sem verið er að vinna í
Git log
-	Birtir commit söguna fyrir repo-ið
o	Hvaða commits hafa verið gerð
o	Hver gerði hvaða commit
o	Skilaboðin fyrir commitið
Git checkout -<file_name>
-	Discards changes in the working directory. It reverts the specified file to the state of the last commit

Forking a repository
-	To fork a repo þýðir að búa til sína eigin útgáfu af repo sem annar er með á sínu GitHub
o	Gerir þér kleyft að gera breytingar á því án þess að hafa áhrif á upprunalega skjalið
-	Gert á GitHub síðunni með því að ýta á “Fork” hnappinn

Making a pull request
-	Gerir þér kleyft að láta verkefnastjóra vita af þeim breytingum sem þú hefur push-að í fork eða grein í GitHub safninu
-	Stjórnandi getur farið yfir breytingarnar áður en þær eru sameinaðar (merge) við aðalskjalið
-	Býr til pull request á GitHub vefsíðunni með því að fara í repo-ið og ýta á “new pull request” takkann

Code review
-	Ferlið þar sem aðrir hópmeðlimir skoða pull request-ið og koma með athugasemdir (ef það eru einhverjar) áður en breytingarnar eru sameinaðar.
o	Hjálpar við að halda gæðunum í kóðanum og að eitthvað sem á ekki að fara í aðalkóðann fari í hann.
Árekstrar
-	Árekstrar (conflict) geta komið upp ef breytingar hafa verið gerða á sömu línum í sömu skrám
-	Dæmi: 
o	Main inniheldur línuna: print(“Hello world”)
o	Feature branch breytir línunni í: print(“Hello Git”)
o	Þegar við reynum að merge-a þá veit Git ekki hvaða útgáfu hann á að velja
o	Lausn: opna skránna og ákveða hora línunna við viljum halda, eða báðar. Vista og commit-a síðan rétta lausn
-	Rangt branch --> nota ‘git checkout <branch_name>’ eða ‘git switch <branch_name>’
-	Gleymt að gera pull áður en push --> nota ‘git pull’ til að sækja nýjustu breytingar áður en push

Styttri útskýringar
-	git init: Initializing a new Git repository in a project directory.
-	Working Directory, Staging Area, and Repository: Understanding the three states of files in Git.
-	git add: Staging changes to be included in the next commit.
-	git status: Checking the current state of the working directory and staging area.
-	git commit: Saving staged changes to the repository with a descriptive message.
-	git log: Viewing the commit history.
-	git clone: Copying a remote repository to your local machine.
-	git remote add origin: Connecting a local repository to a remote one.
-	git push: Sending local commits to the remote repository.
-	git pull: Fetching and integrating changes from the remote repository.
-	git branch: Creating, listing, and deleting branches.
-	git checkout: Switching between branches or restoring files.
-	git merge: Combining changes from different branches.
-	git config: Setting user information (name, email) for commits.
-	.gitignore: Specifying files or directories to be ignored by Git.

