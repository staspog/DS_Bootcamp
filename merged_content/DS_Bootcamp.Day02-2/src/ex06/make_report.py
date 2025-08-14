from analytics import Research
from config import TELEGRAM_WEBHOOK_URL, TELEGRAM_CHAT_ID, report_template, num_of_steps
import sys
import logging

def main():
    research = None
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python make_report.py <data_file>")
        
        research = Research(sys.argv[1])
        data = research.file_reader()
        
        analytics = research.Analytics(data)
        heads, tails = analytics.counts()
        heads_pct, tails_pct = analytics.fractions()
        
        predictions = analytics.predict_random(num_of_steps)
        predicted_heads = sum(p[0] for p in predictions)
        predicted_tails = sum(p[1] for p in predictions)
        
        report = report_template.format(
            observations=len(data),
            heads=heads,
            tails=tails,
            heads_pct=heads_pct,
            tails_pct=tails_pct,
            n=num_of_steps,
            predicted_heads=predicted_heads,
            predicted_tails=predicted_tails
        )
        
        analytics.save_file(report, "report", "txt")
        print(report)
        research.send_telegram(True)
        
    except Exception as e:
        logging.error(f"Critical error: {str(e)}")
        if research:
            research.send_telegram(False)
        sys.exit(1)

if __name__ == '__main__':
    main()