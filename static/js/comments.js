const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
var deleteButtons = document.getElementsByClassName("btn-delete");
var deleteConfirm = document.getElementById("deleteConfirm");


for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        console.log(button)
        let postId = e.target.getAttribute("post_id");
        deleteConfirm.href = `/delete/${postId}`;
        deleteModal.show();
    });
}
// #code taken from django blog walkthrough webinar