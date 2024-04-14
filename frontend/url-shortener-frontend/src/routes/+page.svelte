<script>
    import { DateInput } from 'date-picker-svelte'
	let date = new Date()
    let url = 'https://daisyui.com';
    let url_short = 'something';

    const submit = async () => {
        // const res = await fetch('http://localhost:3000/api/short', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({
        //         url: url,
        //         url_short: url_short,
        //         date: date
        //     })
        // })
        // const data = await res.json()
        console.log(url, url_short, date)
    }
</script>


<div class="container p-16 flex-row flex justify-between">
    <div>
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">Long Url you want to short</span>
            </div>
            <input type="text" placeholder="url" class="input input-bordered w-full max-w-xs" bind:value={url}/>
        </label>
        <label class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">Prefix shorted url</span>
            </div>
            <input type="text" placeholder="url-short" class="input input-bordered w-full max-w-xs" bind:value={url_short}/>
        </label>
        <span class="form-control w-full max-w-xs">
            <div class="label">
                <span class="label-text">Expired Date</span>
            </div>
            <DateInput 
            format="dd/MM/yyyy"
            placeholder="Select a date"
            bind:value={date} 
            required={true}
            dynamicPositioning={true}
            closeOnSelection={true}/>
        </span>

        <button class="btn btn-primary mt-4" on:click={submit}>Short Url</button>
    </div>
    
    <div class="mockup-browser border border-base-300">
        <div class="mockup-browser-toolbar">
            <div class="input border border-base-300">{url}</div>
        </div>
        <div class="flex justify-center px-4 py-16 border-t border-base-300">will be short into lit.web.id/{url_short}</div>
    </div>
</div>