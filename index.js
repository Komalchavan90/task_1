const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({ headless: true }); 
    const page = await browser.newPage(); 

    
    await page.goto("https://gitlab.industrysoftware.automation.siemens.com/ActiveWorkspace/docs/-/wikis/AW-Patch-to-SWF-branch-mapping", {
        waitUntil: "networkidle2"
    });

    const dataMap = await page.evaluate(() => {
        const map = new Map();


        const rows = document.querySelectorAll("table tbody tr");

        rows.forEach(row => {
            const awCell = row.children[1]?.innerText.trim(); // AW column (2nd column)
          //   console.log(awCell)
            const swfCell = row.children[2]?.innerText.trim(); // SWF column (3rd column)
          //   console.log(swfCell)

            if (awCell && swfCell) {
                map.set(awCell, swfCell); 
            }
        });

        return Object.fromEntries(map);
    });

    console.log("AW to SWF Mapping:", dataMap);

    await browser.close(); 
})();
