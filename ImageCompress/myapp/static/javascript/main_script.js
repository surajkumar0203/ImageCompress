const btn=document.querySelector('button')
const input = document.querySelector("input");
const drop_box=document.querySelector(".drop_box")

btn.addEventListener('click',(e)=>{
    input.click()
    
})

input.addEventListener('change',(e)=>{
    const filename=e.target.files[0].name
    const extention=filename.split(".")[1]
    if(extention !=='jpg' && extention !=='png' && extention !=='jpeg'){
        document.getElementById('msg').innerText="unsupported file"
    }else{
        const imageUrl = URL.createObjectURL(e.target.files[0])
        const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
        
        drop_box.innerHTML=`
            <form method="POST" enctype="multipart/form-data">
                <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}"/>
                <div>
                    <img src="${imageUrl}" alt="${imageUrl}" width=100 height=100 />
                    <p class="image_name">${filename}</p>
                </div>
                <input type="file" name="images" id="hiddenImageInput" style="display: none;" />
                <button type="submit" class="btn">Upload</button>
            </form>
        `

        // Set the file input's file to the selected image file
        const hiddenImageInput = document.getElementById('hiddenImageInput');
        const dataTransfer = new DataTransfer();
       
        dataTransfer.items.add(e.target.files[0]);
      
        hiddenImageInput.files = dataTransfer.files;
    }
})


