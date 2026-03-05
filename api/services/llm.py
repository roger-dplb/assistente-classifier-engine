"""
LLM integration service using OpenAI API.
"""
import openai
from api.core.config import settings

# Configure OpenAI client
client = openai.AsyncOpenAI(api_key=settings.OPENAI_API_KEY)


async def generate_completion(
    prompt: str,
    model: str = None,
    temperature: float = 0.3,
    max_tokens: int = 2000
) -> str:
    """
    Generate a completion using OpenAI API.
    
    Args:
        prompt: The prompt to send to the LLM
        model: Model to use (defaults to settings.OPENAI_MODEL)
        temperature: Sampling temperature (0-2)
        max_tokens: Maximum tokens in response
        
    Returns:
        Generated text response
    """
    model = model or settings.OPENAI_MODEL
    
    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in analyzing customer service interactions."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=settings.LLM_TIMEOUT
        )
        
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"LLM generation failed: {str(e)}")


async def generate_structured_output(
    prompt: str,
    model: str = None,
    temperature: float = 0.1
) -> dict:
    """
    Generate structured JSON output using OpenAI API.
    
    Args:
        prompt: The prompt to send (should request JSON output)
        model: Model to use
        temperature: Lower temperature for consistency
        
    Returns:
        Parsed JSON response as dict
    """
    import json
    
    # Append JSON instruction if not present
    if "json" not in prompt.lower():
        prompt += "\n\nRespond ONLY with valid JSON."
    
    response_text = await generate_completion(
        prompt=prompt,
        model=model,
        temperature=temperature
    )
    
    # Try to extract JSON from response
    try:
        # Look for JSON in code blocks
        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_str = response_text.split("```")[1].split("```")[0].strip()
        else:
            json_str = response_text.strip()
        
        return json.loads(json_str)
    except (json.JSONDecodeError, IndexError) as e:
        raise Exception(f"Failed to parse JSON from LLM response: {str(e)}")
