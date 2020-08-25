const fs = require('fs');
const yaml = require('js-yaml');

// This is a WIP - see python version instead

try {
    let fileContents = fs.readFileSync('../helm/prod-ecommerce-values.yaml', 'utf8');
    let helm = yaml.safeLoadAll(fileContents);

    console.log(helm);
} catch (error) {
    console.error(error);
}