function poll_endpoint_ph() {
        let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                let text = xhttp.responseText
                let response = JSON.parse(xhttp.responseText)
                document.getElementById("ph").className = "row ph"
                txt = document.getElementById("ph_level")
                txt.innerHTML = ""
                txt.innerText = response["ph_level"]

            }
        };
        xhttp.open("POST", "/service/poll", true);
        xhttp.send();
        poll_handle = setTimeout(function () {
            poll_endpoint()
        }, 4000);
    }

function poll_endpoint_ph_tank() {
        let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                let text = xhttp.responseText
                let response = JSON.parse(xhttp.responseText)
                document.getElementById("ph_tank").className = "row ph"
                txt = document.getElementById("ph_tank_level")
                txt.innerHTML = ""
                txt.innerText = response["ph_tank_level"]

            }
        };
        xhttp.open("POST", "/service/poll", true);
        xhttp.send();
        poll_handle = setTimeout(function () {
            poll_endpoint()
        }, 4000);
    }