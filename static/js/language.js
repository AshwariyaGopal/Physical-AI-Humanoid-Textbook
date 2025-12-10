// static/js/language.js
window.switchLanguage = async (lang) => {
  if (lang === 'en') {
    // If switching to English, reload the page to default language or handle client-side
    // translation back to English if you have original content stored.
    // For simplicity, we'll reload, assuming Docusaurus default is English.
    window.location.reload();
    return;
  }

  // Get the content of the main content area (you might need to adjust the selector)
  const contentElement = document.querySelector('.main-wrapper'); 
  if (!contentElement) {
    console.error('Main content element not found for translation.');
    return;
  }

  const originalContent = contentElement.innerHTML;

  try {
    const response = await fetch('/api/translate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: originalContent, target_lang: lang }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    
    // Update the content with the translated text
    contentElement.innerHTML = data.translated_text;

  } catch (error) {
    console.error('Error during translation:', error);
    alert('Translation failed. Please try again later.');
  }
};