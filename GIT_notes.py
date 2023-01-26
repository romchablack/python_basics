# HELP
git add --help

# MANUAL
man git

# STATUS
git status # check current status

# display files and folders
ls
ls -la

# LOG
git log
git log --online
git log --oneline --decorate --graph --all

# create Repo
git init

# clone repo
git clone <url>

# Add file to Stage
git add .   # add ALL files

git commit
git commit -m "some text for comit"
git commit -a ""


**************** WRONG ****************

# rename from "filename1" to "filename2"
mv filename1 filename2
git add filename1 # confirm delete
git add filename2 # confirm add

# delete
rm filename1
git add filename1 # confirm delete

**************** CORRECT ****************

# rename from "filename1" to "filename2"
git mv filename1 filename2

# delete
git rm filename1

# Change commit message and/or add files to the latest commit
git commit --amend
git commit --amend --no-edit          # update commit w/o modifying commit message

# Delete file from commit
git rm <filename>
git commit --amend --no-edit

# new branch
1) 
git branch <new_branch_name>
git checkout <new_branch_name>
2) 
git checkout -b <new_branch_name>



-------------------------------------------




###### Настройка ######

# Установка в Linux
Если же у вас дистрибутив, основанный на Debian, например, Ubuntu, попробуйте apt:
    sudo apt install git

# Посмотреть все установленные настройки
    git config --list
    git config --list --show-origin
    git config --global user.name "Norman Swartz"
    git config --global user.email normanshwartz@gmail.com

# Настройка ветки по умолчанию
    git config --global init.defaultBranch main

# Проверка настроек
    git config --list
    git config user.name

# Как получить помощь?
    git help <команда>
    git <команда> --help 
    man git-<команда>

# Выбор редактора
    git config --global core.editor emacs
    git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"

###### REPOS ######
# Create Git-repository
    cd /home/user/my_project
    git init

# Clone existing repo (SSH)
    cd /home/user/my_project
    git clone git@github.com:romchablack/rchornyi_automation_course_23.git

# Check status
    git status
    git status -s 
    git status --short

# Track new/modified files
    git add <file or folder name>

# Ignore files
    создать файл .gitignore. с перечислением шаблонов соответствующих таким файлам. Вот пример файла .gitignore:
    
    $ cat .gitignore
    *.[oa]
    
    Первая строка предписывает Git игнорировать любые файлы заканчивающиеся на «.o» или «.a» — объектные и архивные файлы, которые могут появиться во время сборки кода. Вторая строка предписывает игнорировать все файлы заканчивающиеся на тильду (~),

# Review staged and unstaged changes
    $ git diff
    diff --git a/CONTRIBUTING.md b/CONTRIBUTING.md
    index 8ebb991..643e24f 100644
    --- a/CONTRIBUTING.md
    +++ b/CONTRIBUTING.md
    @@ -65,7 +65,8 @@ branch directly, things can get messy.
    Please include a nice description of your changes when you submit your PR;
    if we have to read the whole diff to figure out why you're contributing
    in the first place, you're less likely to get feedback and have your change
    -merged in.
    +merged in. Also, split your changes into comprehensive chunks if you patch is
    +longer than a dozen lines.

    If you are starting to work on a particular area, feel free to submit a PR
    that highlights your work in progress (and note in the PR title that it's

    git diff --staged
    Если вы хотите посмотреть, что вы проиндексировали и что войдёт в следующий коммит, вы можете выполнить 

# Commit changes
    git commit -m "commit message"
    git commit -a
    Добавление параметра -a в команду git commit заставляет Git автоматически индексировать каждый уже отслеживаемый на момент коммита файл, позволяя вам обойтись без git add

# Delete files
    git rm --cached README
    git commit -m "file was deleted"

# Move files
    git mv file_from file_to # rename file

# Операции отмены



# Просмотр удалённых репозиториев
    Для того, чтобы просмотреть список настроенных удалённых репозиториев, вы можете запустить команду git remote

# Добавление удалённых репозиториев # 
    В предыдущих разделах мы уже упоминали и приводили примеры добавления удалённых репозиториев, сейчас рассмотрим эту операцию подробнее. Для того, чтобы добавить удалённый репозиторий и присвоить ему имя (shortname), просто выполните команду git remote add <shortname> <url>:

# Получение изменений из удалённого репозитория — Fetch и Pull
    git fetch [remote-name] - ### git clone = git fetch
    Данная команда связывается с указанным удалённым проектом и забирает все те данные проекта, которых у вас ещё нет. После того как вы выполнили команду, у вас должны появиться ссылки на все ветки из этого удалённого проекта, которые вы можете просмотреть или слить в любой момент.

    git fetch origin извлекает все наработки, отправленные на этот сервер после того, как вы его клонировали (или получили изменения с помощью fetch).

    git pull = git fetch + git merge

# Отправка изменений в удаленный репозиторий (Push)
    Когда вы хотите поделиться своими наработками, вам необходимо отправить их в удалённый репозиторий. Команда для этого действия простая: git push <remote-name> <branch-name>. Чтобы отправить вашу ветку master на сервер origin (повторимся, что клонирование обычно настраивает оба этих имени автоматически), вы можете выполнить следующую команду для отправки ваших коммитов:

    git push origin master (or git push origin main)

# Удаление и переименование удалённых репозиториев
    Для переименования удалённого репозитория можно выполнить git remote rename. Например, если вы хотите переименовать pb в paul, вы можете это сделать при помощи git remote rename:

    git remote rename pb paul
    git remote
    origin
    paul
    
    Если по какой-то причине вы хотите удалить удаленный репозиторий — вы сменили сервер или больше не используете определённое зеркало, или кто-то перестал вносить изменения — вы можете использовать git remote rm:

    git remote remove paul
    git remote
    origin