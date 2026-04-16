SCENARIOS = [
    {
        "id": 1,
        "intent": "Follow up after a client discovery meeting",
        "tone": "formal",
        "facts": [
            "Meeting happened on Tuesday",
            "Client is interested in workflow automation",
            "Need to send the pricing deck by Friday",
            "Ask for a follow-up call next week",
        ],
        "reference_email": """Subject: Follow-Up and Next Steps

Dear Client,

Thank you for meeting with us on Tuesday. It was great to learn more about your interest in workflow automation and the goals your team is working toward.

As discussed, I will send the pricing deck by Friday for your review. I would also like to schedule a follow-up call next week to discuss the next steps.

Please let me know your availability.

Best regards,
[Your Name]""",
    },
    {
        "id": 2,
        "intent": "Request deadline extension for a project submission",
        "tone": "empathetic",
        "facts": [
            "The delay was caused by unexpected data issues",
            "Need a 2-day extension",
            "Current deadline is Thursday",
            "Can submit the final version by Saturday morning",
        ],
        "reference_email": """Subject: Request for Brief Extension on Project Submission

Dear [Recipient Name],

I hope you are doing well. We encountered unexpected data issues while finalizing the project, which has impacted our timeline.

I would like to request a brief two-day extension. The current deadline is Thursday, and I can submit the final version by Saturday morning.

I appreciate your understanding.

Sincerely,
[Your Name]""",
    },
    {
        "id": 3,
        "intent": "Ask vendor for revised proposal",
        "tone": "formal",
        "facts": [
            "Budget cap is 8 lakhs",
            "Need support coverage for 12 months",
            "Original proposal exceeded budget",
            "Request revised proposal by Monday",
        ],
        "reference_email": """Subject: Request for Revised Proposal

Dear [Vendor Name],

Thank you for sharing the initial proposal. After reviewing it internally, we found the pricing exceeds our budget cap of 8 lakhs.

Could you please send a revised proposal within this budget, including 12 months of support coverage, by Monday?

Best regards,
[Your Name]""",
    },
    {
        "id": 4,
        "intent": "Apologize to a customer for delayed response",
        "tone": "empathetic",
        "facts": [
            "Response was delayed by 3 business days",
            "Issue relates to account access",
            "Problem is now resolved",
            "Offer help if issue happens again",
        ],
        "reference_email": """Subject: Apology for the Delay and Account Access Update

Dear [Customer Name],

I sincerely apologize for the delayed response over the past 3 business days. I understand your account access issue was important and appreciate your patience.

I'm glad to confirm the problem is now resolved. Please feel free to reach out if the issue occurs again.

Kind regards,
[Your Name]""",
    },
    {
        "id": 5,
        "intent": "Remind team to complete compliance training",
        "tone": "urgent",
        "facts": [
            "Training deadline is tomorrow 5 PM",
            "Three team members have not completed it",
            "Completion is mandatory",
            "Ask them to confirm once done",
        ],
        "reference_email": """Subject: Urgent: Complete Compliance Training by Tomorrow

Hi Team,

This is a reminder that the compliance training deadline is tomorrow at 5 PM. Three team members have not yet completed it.

Completion is mandatory. Please finish it as soon as possible and confirm once done.

Best,
[Your Name]""",
    },
    {
        "id": 6,
        "intent": "Thank an interviewer after an interview",
        "tone": "formal",
        "facts": [
            "Interview was for AI Engineer role",
            "Discussed prompt engineering and evaluation systems",
            "Reinforce strong interest in the role",
            "Thank them for their time",
        ],
        "reference_email": """Subject: Thank You for the Interview

Dear [Interviewer Name],

Thank you for taking the time to speak with me about the AI Engineer role. I especially enjoyed our discussion on prompt engineering and evaluation systems.

The conversation has reinforced my strong interest in the role. Thank you again for your time and consideration.

Best regards,
[Your Name]""",
    },
    {
        "id": 7,
        "intent": "Inform manager about planned leave",
        "tone": "casual",
        "facts": [
            "Leave dates are May 12 to May 14",
            "All critical tasks will be completed before leave",
            "Rahul will be backup contact",
            "Ask for approval",
        ],
        "reference_email": """Subject: Planned Leave Request — May 12 to 14

Hi [Manager Name],

I wanted to let you know I'm planning to take leave from May 12 to May 14. I'll complete all critical tasks before then, and Rahul will be the backup contact.

Please let me know if you're okay approving this.

Thanks,
[Your Name]""",
    },
    {
        "id": 8,
        "intent": "Request internal referral from a former colleague",
        "tone": "casual",
        "facts": [
            "Applying for Data Scientist role",
            "Job was posted yesterday",
            "Resume is updated",
            "Can share job link and resume if helpful",
        ],
        "reference_email": """Subject: Referral Request for Data Scientist Role

Hi [Colleague Name],

Hope you're doing well! I noticed a Data Scientist role at your company posted yesterday and I'm planning to apply. My resume is up to date, and I'm happy to share both the job link and resume if that helps.

If you're comfortable, I'd really appreciate a referral.

Thanks so much,
[Your Name]""",
    },
    {
        "id": 9,
        "intent": "Notify stakeholder about launch delay",
        "tone": "formal",
        "facts": [
            "Launch moved from April 18 to April 25",
            "Delay caused by final security review",
            "No impact on agreed feature scope",
            "Will send revised rollout plan tomorrow",
        ],
        "reference_email": """Subject: Update on Launch Timeline

Dear [Stakeholder Name],

I wanted to share an update on the launch timeline. The launch has been moved from April 18 to April 25 due to the final security review.

There is no impact on the agreed feature scope. I will send the revised rollout plan tomorrow.

Best regards,
[Your Name]""",
    },
    {
        "id": 10,
        "intent": "Ask finance team about reimbursement status",
        "tone": "formal",
        "facts": [
            "Claim submitted on March 28",
            "Amount is Rs. 12,450",
            "Travel reimbursement for client visit",
            "Request status update",
        ],
        "reference_email": """Subject: Request for Reimbursement Status Update

Dear Finance Team,

I am writing to request a status update on my reimbursement claim submitted on March 28. The amount is Rs. 12,450, for travel expenses related to a client visit.

Please let me know if any additional information is needed.

Best regards,
[Your Name]""",
    },
]