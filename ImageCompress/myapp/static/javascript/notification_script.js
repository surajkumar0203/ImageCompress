const notification = document.getElementById('notification');


if(notification){
    // Automatically hide the notification after 3 seconds
    setTimeout(hideNotification, 3000);
    function hideNotification() {
       notification.classList.remove('show');
    }
    document.getElementById('close-btn').addEventListener('click', hideNotification);

}