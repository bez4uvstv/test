git init --> превращает текущую директорию в git репозиторий (создается директория .git)
git add .(. - все файлы, можно указать отдельные файлы) --> отслеживание всех файлов
git commit -m "commit"--> добавляет /соверщает сохранение в git всех фалов , которые находятся в индексе 
git log --> выводит журнал сохранений
git status --> показывает статус наших файлов
git remote add origin <SSH>(ссылка на репозиторий в gitHub) - создает связь git с gitHub
git checkout hash_commit --> переключаемся к нужной версии
git branch --> выводит список всех веток в проекте (зведочкой помечена ваша активная ветка) если указать название то можно создать
git switch <название ветки>/ git checkout <название ветки> --> переход на указанную ветку
git push origin(название связи) master(название ветки) --> отправка версии кода на удаленный репозиторий (gitHub)

git clone <ссылка на проект удаленный проект> --> скопировать скачать репозиторий

