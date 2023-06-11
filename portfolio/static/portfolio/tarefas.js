document.addEventListener('DOMContentLoaded', function () {
        document.querySelector('form').onsubmit = () => {
            const task = document.querySelector('#task').value;

            const li = document.createElement('li');
            li.innerHTML = task;
            document.querySelector('#tasks').append(li)

            document.querySelector('#task').value = '';
        }
    }
)