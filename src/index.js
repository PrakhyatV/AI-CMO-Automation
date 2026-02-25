import dotenv from 'dotenv';
import { ContentGenerator } from './workflows/contentGenerator.js';
import { CampaignManager } from './workflows/campaignManager.js';

dotenv.config();

console.log('🚀 AI CMO Automation Starting...');

// Main orchestration logic
async function main() {
  try {
    console.log('✅ AI CMO Automation is ready!');
    console.log('📊 Available workflows:');
    console.log('  - Content Generation');
    console.log('  - Campaign Management');
    console.log('  - Social Media Automation');
    
    // Example: Generate content
    // const generator = new ContentGenerator();
    // await generator.generateBlogPost('AI in Marketing');
    
  } catch (error) {
    console.error('❌ Error:', error.message);
  }
}

main();
