git remote add "origin" "https://github.com/jarryzeng/git.git"
git add .

call "./set time.bat"

git commit -m %year%-%month%-%day%.%hour%:%min%
git push
git remote remove "origin"